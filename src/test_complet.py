from .debruitage.debruitage import denoising_image
from .bruitage.bruitage import generate_noisy_image
import matplotlib.pyplot as plt
from src.snr import get_snr
import os
import re
from src.image_management import load_image


def tracer_poivre_et_sel(results):
    rates = [item["rate"] for item in results["poivre_et_sel"]]
    snrs = [item["snr"] for item in results["poivre_et_sel"]]

    plt.figure(figsize=(10, 6))
    plt.plot(rates, snrs, marker='o', linestyle='-', label='Salt and Pepper Noise')
    plt.title('Bruit poivre et sel: Taux de bruitage vs SNR')
    plt.xlabel('Pourcentage (%)')
    plt.ylabel('SNR (dB)')
    plt.grid(True)
    plt.legend()
    plt.show()


def tracer_bruit_additif(results):
    # Regrouper les données par moyenne
    grouped_data = {}
    for item in results["additif"]:
        mean = item["mean"]
        if mean not in grouped_data:
            grouped_data[mean] = {"std_devs": [], "snrs": []}
        grouped_data[mean]["std_devs"].append(item["std_dev"])
        grouped_data[mean]["snrs"].append(item["snr"])

    # Tracer une courbe pour chaque moyenne
    plt.figure(figsize=(10, 6))
    for mean, data in grouped_data.items():
        plt.plot(data["std_devs"], data["snrs"], marker='o', label=f"Moyenne: {mean:.1f}")

    # Ajouter les détails du graphique
    plt.title("Bruit Additif : Écart-type vs SNR pour différentes moyennes")
    plt.xlabel("Écart-type")
    plt.ylabel("SNR (dB)")
    plt.grid(True)
    plt.legend(title="Moyenne", loc="best")
    plt.show()


def tracer_bruit_multiplicatif(results):
    # Regrouper les données par moyenne
    grouped_data = {}
    for item in results["multiplicatif"]:
        mean = item["mean"]
        if mean not in grouped_data:
            grouped_data[mean] = {"std_devs": [], "snrs": []}
        grouped_data[mean]["std_devs"].append(item["std_dev"])
        grouped_data[mean]["snrs"].append(item["snr"])

    # Tracer une courbe pour chaque moyenne
    plt.figure(figsize=(10, 6))
    for mean, data in grouped_data.items():
        plt.plot(data["std_devs"], data["snrs"], marker='o', label=f"Moyenne: {mean:.1f}")

    # Ajouter les détails du graphique
    plt.title("Bruit Multiplicatif : Écart-type vs SNR pour différentes moyennes")
    plt.xlabel("Écart-type")
    plt.ylabel("SNR (dB)")
    plt.grid(True)
    plt.legend(title="Moyenne", loc="best")
    plt.show()


def tracer_denoising_results(results, denoise_name):
    # Extraire les données pour la méthode médiane
    snr_attendus = [item["snr_attendu"] for item in results]
    snr_obtenus = [item["snr_obtenu"] for item in results]

    # Créer un scatter plot avec une ligne idéale y = x
    plt.figure(figsize=(10, 6))
    plt.scatter(snr_attendus, snr_obtenus, color="blue", label=f"SNR obtenu ({denoise_name})")
    plt.plot(snr_attendus, snr_attendus, color="red", linestyle="--", label="SNR idéal (y = x)")

    # Ajouter des annotations pour les points divergents
    for attendu, obtenu in zip(snr_attendus, snr_obtenus):
        if abs(attendu - obtenu) > 1:  # Seuil de divergence pour annotation
            plt.annotate(f"{obtenu:.1f}", (attendu, obtenu), textcoords="offset points", xytext=(5, -10), ha="center")

    # Configurer le graphique
    plt.title(f"Comparaison entre SNR attendu et obtenu après débruitage ({denoise_name})")
    plt.xlabel("SNR attendu (dB)")
    plt.ylabel("SNR obtenu (dB)")
    plt.grid(True)
    plt.legend(loc="best")
    plt.tight_layout()
    plt.show()


def test_complet():
    image = "images_reference/lenaNB.tiff"
    print("Test complet de bruitage et débruitage d'images\n")
    results = {"poivre_et_sel": [], "additif": [], "multiplicatif": []}

    print("Génération d'images bruitées\n")

    print("Bruit poivre et sel\n")
    for i in range(0, 101, 5):
        results["poivre_et_sel"].append(
            {"rate": i, "snr": generate_noisy_image("p", "Salt and Pepper Noise", image, display=False, rate=i)}
        )
    print("\n")
    print(results["poivre_et_sel"])

    print("Bruit additif\n")
    # Pour le bruit additif, on prend une moyenne de entre -0.5 et 0.5 et un écart-type entre 0.01 et 0.1
    for i in range(0, 11):
        for j in range(0, 11):
            if i == 0 and j == 0:
                continue
            mean = i / 10 - 0.5
            std_dev = j / 100
            print(f"mean: {mean}, std_dev: {std_dev}")
            results["additif"].append(
                {"mean": mean, "std_dev": std_dev, "snr": generate_noisy_image("a", "Additive Noise", image, display=False, mean=mean, std_dev=std_dev)}
            )
    print("\n")
    print(results["additif"])

    print("Bruit multiplicatif\n")
    # Pour le bruit additif, on prend une moyenne de entre -0.5 et 0.5 et un écart-type entre 0.01 et 0.1
    for i in range(0, 11):
        for j in range(0, 11):
            if i == 0 and j == 0:
                continue
            mean = i / 10 - 0.5
            std_dev = j / 100
            print(f"mean: {mean}, std_dev: {std_dev}")
            results["multiplicatif"].append(
                {"mean": mean, "std_dev": std_dev, "snr": generate_noisy_image("m", "Multiplicative Noise", image, display=False, mean=mean, std_dev=std_dev)}
            )

    print("\n")
    print(results["multiplicatif"])

    tracer_poivre_et_sel(results)
    tracer_bruit_additif(results)
    tracer_bruit_multiplicatif(results)

    print("Fin de test complet de bruitage")

    print("Débruitage d'image\n")
    print("Image ref 1\n")
    results = {"median3x3": [], "convolution3x3": [], "median5x5": [], "convolution5x5": []}

    images_bruitees = [f for f in os.listdir("images_reference") if f.startswith("image1_bruitee_snr_")]

    for image_bruitee in images_bruitees:
        match = re.search(r"_snr_(\d+\.\d+)", image_bruitee)
        if match:
            snr_attendu = float(match.group(1))  # Convertir en float pour faciliter les calculs
            snr_obtenu_median_3 = denoising_image(
                arg="m", denoise_name="Médian", image_path=f"images_reference/{image_bruitee}",
                display=False, taille_voisinage=1
            )
            snr_obtenu_median_5 = denoising_image(
                arg="m", denoise_name="Médian", image_path=f"images_reference/{image_bruitee}",
                display=False, taille_voisinage=2
            )
            snr_obtenu_convolution_3 = denoising_image(
                arg="c", denoise_name="Convolution", image_path=f"images_reference/{image_bruitee}",
                display=False, taille_voisinage=1
            )
            snr_obtenu_convolution_5 = denoising_image(
                arg="c", denoise_name="Convolution", image_path=f"images_reference/{image_bruitee}",
                display=False, taille_voisinage=2
            )
            results["median3x3"].append({"snr_attendu": snr_attendu, "snr_obtenu": snr_obtenu_median_3})
            results["median5x5"].append({"snr_attendu": snr_attendu, "snr_obtenu": snr_obtenu_median_5})
            results["convolution3x3"].append({"snr_attendu": snr_attendu, "snr_obtenu": snr_obtenu_convolution_3})
            results["convolution5x5"].append({"snr_attendu": snr_attendu, "snr_obtenu": snr_obtenu_convolution_5})

    tracer_denoising_results(results["median3x3"], "Médian 3x3")
    tracer_denoising_results(results["median5x5"], "Médian 5x5")
    tracer_denoising_results(results["convolution3x3"], "Convolution 3x3")
    tracer_denoising_results(results["convolution5x5"], "Convolution 5x5")

    print("Image ref 2\n")
    results = {"median3x3": [], "convolution3x3": [], "median5x5": [], "convolution5x5": []}
    image_ref = "images_reference/image2_reference.png"
    images_bruitees = [f for f in os.listdir("images_reference") if f.startswith("image2_bruitee_sigma")]

    for image_bruitee in images_bruitees:
        snr_attendu = get_snr(load_image(f"images_reference/{image_bruitee}"), load_image(image_ref))
        snr_obtenu_median_3 = denoising_image(
                arg="m", denoise_name="Médian", image_path=f"images_reference/{image_bruitee}",
                display=False, taille_voisinage=1
            )
        snr_obtenu_median_5 = denoising_image(
                arg="m", denoise_name="Médian", image_path=f"images_reference/{image_bruitee}",
                display=False, taille_voisinage=2
            )
        snr_obtenu_convolution_3 = denoising_image(
                arg="c", denoise_name="Convolution", image_path=f"images_reference/{image_bruitee}",
                display=False, taille_voisinage=1
            )
        snr_obtenu_convolution_5 = denoising_image(
                arg="c", denoise_name="Convolution", image_path=f"images_reference/{image_bruitee}",
                display=False, taille_voisinage=2
            )
        results["median3x3"].append({"snr_attendu": snr_attendu, "snr_obtenu": snr_obtenu_median_3})
        results["median5x5"].append({"snr_attendu": snr_attendu, "snr_obtenu": snr_obtenu_median_5})
        results["convolution3x3"].append({"snr_attendu": snr_attendu, "snr_obtenu": snr_obtenu_convolution_3})
        results["convolution5x5"].append({"snr_attendu": snr_attendu, "snr_obtenu": snr_obtenu_convolution_5})

    tracer_denoising_results(results["median3x3"], "Médian 3x3")
    tracer_denoising_results(results["median5x5"], "Médian 5x5")
    tracer_denoising_results(results["convolution3x3"], "Convolution 3x3")
    tracer_denoising_results(results["convolution5x5"], "Convolution 5x5")

    print("Fin de test complet de débruitage")

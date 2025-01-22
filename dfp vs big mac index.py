import matplotlib.pyplot as plt
import seaborn as sns

# Configuration de Seaborn pour améliorer la visibilité
sns.set_theme(style="whitegrid")

# Données pour les années (2005 à 2024)
years = list(range(2005, 2025))

# Indemnisation pour 1 % de DFP (en euros)
dfp_values = [
    1000, 1020, 1040, 1060, 1080, 1200, 1210, 1225, 1235, 1250, 1300, 
    1325, 1340, 1350, 1350, 1400, 1425, 1450, 1480, 1500
]

# Données pour les produits
products = {
    "Big Mac": {
        "prices": [2.90, 3.00, 3.10, 3.20, 3.30, 3.50, 3.55, 3.60, 3.70, 3.90, 4.00, 
                   4.10, 4.20, 4.30, 4.20, 4.50, 4.70, 4.40, 5.00, 5.00],
        "color_price": "orange",
        "color_count": "green",
        "title": "Évolution de l'indemnisation DFP et du Big Mac (2005-2024)"
    },
    "Coca-Cola": {
        "prices": [1.00, 1.05, 1.10, 1.15, 1.20, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 
                   1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 2.00, 2.10],
        "color_price": "red",
        "color_count": "purple",
        "title": "Évolution de l'indemnisation DFP et du Coca-Cola (2005-2024)"
    },
    "Baguette": {
        "prices": [0.80, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96, 1.00, 1.05, 
                   1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50],
        "color_price": "brown",
        "color_count": "gold",
        "title": "Évolution de l'indemnisation DFP et du prix de la baguette (2005-2024)"
    },
    "Essence": {
        "prices": [1.20, 1.25, 1.30, 1.40, 1.35, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 
                   1.75, 1.80, 1.85, 1.90, 1.85, 1.90, 1.95, 2.00, 2.05],
        "color_price": "darkorange",
        "color_count": "darkgreen",
        "title": "Évolution de l'indemnisation DFP et du litre d'essence (2005-2024)"
    },
    "Ticket de cinéma": {
        "prices": [
            8.00, 8.10, 8.20, 8.30, 8.50, 8.70, 8.90, 9.10, 9.30, 9.50, 9.70, 
            9.90, 10.10, 10.30, 10.50, 10.70, 10.90, 11.10, 11.30, 11.50
        ],
        "color_price": "darkblue",
        "color_count": "skyblue",
        "title": "Évolution de l'indemnisation DFP et du prix du ticket de cinéma (2005-2024)"
    }
}

# Ajout de "Nombre de {product} achetables"
for product, data in products.items():
    prices = data["prices"]
    data["counts"] = [dfp / price for dfp, price in zip(dfp_values, prices)]

# Création de graphiques distincts pour chaque produit
for product, data in products.items():
    prices = data["prices"]
    counts = data["counts"]
    color_price = data["color_price"]
    color_count = data["color_count"]
    title = data["title"]

    # Calcul des pourcentages d'augmentation
    dfp_increase = ((dfp_values[-1] - dfp_values[0]) / dfp_values[0]) * 100
    product_increase = ((prices[-1] - prices[0]) / prices[0]) * 100
    count_increase = ((counts[-1] - counts[0]) / counts[0]) * 100

    plt.figure(figsize=(12, 6))
    
    # Tracé des courbes
    sns.lineplot(x=years, y=dfp_values, marker='o', label="Indemnisation (1% DFP, en €)", color='blue', linestyle='-')
    sns.lineplot(x=years, y=prices, marker='o', label=f"Prix {product} (en €)", color=color_price)
    sns.lineplot(x=years, y=counts, marker='o', label=f"Nombre de {product} achetables", color=color_count, linestyle='--')
    
    # Ajout des annotations pour la première et la dernière année
    plt.text(2005, dfp_values[0] + 50, f"{dfp_values[0]:.0f} €", fontsize=10, ha='center', color='blue', weight='bold')
    plt.text(2024, dfp_values[-1] + 50, f"{dfp_values[-1]:.0f} €", fontsize=10, ha='center', color='blue', weight='bold')
    plt.text(2005, prices[0] - 0.2, f"{prices[0]:.2f} €", fontsize=10, ha='center', color=color_price, weight='bold')
    plt.text(2024, prices[-1] - 0.2, f"{prices[-1]:.2f} €", fontsize=10, ha='center', color=color_price, weight='bold')
    plt.text(2005, counts[0], f"{counts[0]:.1f}", fontsize=10, ha='center', color=color_count, weight='bold')
    plt.text(2024, counts[-1], f"{counts[-1]:.1f}", fontsize=10, ha='center', color=color_count, weight='bold')
    
    # Ajout des pourcentages
    plt.text(2025, dfp_values[-1], f"+{dfp_increase:.1f}%", fontsize=12, color='blue', weight='bold', va='center')
    plt.text(2025, prices[-1], f"+{product_increase:.1f}%", fontsize=12, color=color_price, weight='bold', va='center')
    plt.text(2025, counts[-1], f"{count_increase:.1f}%", fontsize=12, color=color_count, weight='bold', va='center')


    # Configuration du graphique
    plt.title(title, fontsize=16)
    plt.xlabel("Années", fontsize=14)
    plt.ylabel("Valeurs (en € ou unités)", fontsize=14)
    plt.xticks(years, rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()









############################################################################################################################################################################
#imports 
from random import randint

#############################################################################################################################################################################
#Variables globales
NOMBRE_MENU = 6

#############################################################################################################################################################################
#fonctions
def affichage_menu() -> None:
    """
    Affiche le menu
    """
    print("\nVoici la liste d'interaction possible:")
    print("1) Générer un plat aléatoire")
    print("2) Générer une entrée aléatoire")
    print("3) Générer un dessert aléatoire")
    print("4) Générer une boisson sans alcool aléatoire")
    print("5) Générer une boisson avec alcool aléatoire")
    print("6) Générer un plat en choisissant ses ingredients")
    

def saisie_choix()-> int:
    """
    Va proposer à l'utilisateur de chosir une option dans le menu de choix

    Precondition : La saisie est un entier

    Exemple: Aucun sur une fonction de saisie
    """
    choix = int(input("Merci de saisir le chiffre correspondant à votre choix? : "))
    while choix > NOMBRE_MENU or choix < 0:
        choix = int(input(f"Merci de saisir un chiffre entre 1 et {NOMBRE_MENU}: "))
    return choix


def generer_plat_pricipal_aleatoire() -> None:
    """
    Va generer un plat aléatoire

    """

    liste_plat_principaux = ["Poulet rôti", "Pâtes à la carbonara", "Burger", "Sushis", "Salade César", "Pizza", "Risotto", "Curry de légumes", "Steak grillé", "Tacos",
                   "Lasagnes", "Crevettes à l'ail", "Tofu sauté", "Rôti de porc", "Poulet au citron", "Fajitas", "Bœuf Bourguignon", "Tartare de saumon", "Tournedos Rossini", "Magret de canard",
                   "Filet mignon", "Côtes d'agneau", "Rôti de bœuf", "Coq au vin", "Paella", "Escalope de veau", "Poisson en papillote", "Lapin à la moutarde", "Côtelettes de porc", "Boeuf Stroganoff",
                   "Canard à l'orange", "Ratatouille", "Poulet Tikka Masala", "Crevettes grillées", "Truite aux amandes", "Couscous", "Poulet rôti aux herbes", "Poulet Kung Pao", "Hamburger végétarien", "Agneau grillé", "Ailes de poulet épicées",
                   "Chili con carne", "Rôti de dinde", "Côtes de porc BBQ", "Brochettes de poulet", "Ris de veau", "Boulettes de viande", "Lobster Thermidor", "Poulet Parmesan", "Risotto aux champignons",
                   "Poulet Teriyaki", "Poulet au beurre", "Goulash", "Poulet à la moutarde", "Poulet au paprika", "Moussaka", "Côtes de veau", "Barbecue de saucisses", "Sauté de porc", "Côtes levées",
                   "Bœuf haché", "Rôti de porc aux pommes", "Lapin aux pruneaux", "Crevettes créoles", "Poulet cacciatore", "Jarret de porc", "Saumon grillé", "Porc effiloché", "Ratatouille", "Champignons farcis", "Porc au caramel",
                   "Magret de canard au miel", "Poulet à l'ail", "Poulet aux noix de cajou", "Poulet à l'orange", "Saumon en croûte", "Poulet à la thaïlandaise", "Moules marinières", "Rôti de bœuf Wellington", "Tarte au saumon", "Saucisses de porc",
                   "Brochettes de crevettes", "Poulet aux poivrons", "Hamburger classique", "Moules à la crème", "Rôti de dinde aux herbes", "Poulet à la parmigiana", "Poulet au citron vert", "Steak au poivre", "Risotto au safran", "Poulet à la provençale",
                   "Poulet aux olives", "Paella aux fruits de mer", "Fajitas végétariennes", "Poulet Marsala", "Sauté de crevettes", "Tournedos aux champignons", "Bœuf à l'orange", "Boeuf Szechuan", "Poulet aux pêches", "Tofu aux légumes"]
    
    i = randint(0,len(liste_plat_principaux) -1)
    print(f"Le chef vous propose de manger le plat suivant : {liste_plat_principaux[i]} 😋")


def generer_entree_aleatoire() -> str:
    """"
    Va générer une entrée aléatoirement
    """
    
    liste_entree  = ["Salade César", "Soupe à l'oignon", "Calamars frits", "Bruschetta", "Carpaccio de bœuf", "Rillettes de saumon", "Crevettes grillées", "Salade de chèvre chaud", "Huîtres fraîches", "Gaspacho",
                "Mozzarella en carrozza", "Salade niçoise", "Escargots à la bourguignonne", "Potage aux légumes", "Pissaladière", "Ceviche de poisson", "Terrine de foie gras", "Tartare de saumon", "Salade de betteraves", "Asperges grillées",
                "Fondue au fromage", "Salade d'avocat", "Pakoras", "Salade de tomates", "Rouleaux de printemps", "Cocktail de crevettes", "Champignons farcis", "Tartare de bœuf", "Ratatouille", "Poulet frit",
                "Brochettes de poulet", "Salade Waldorf", "Caviar", "Pétoncles poêlés", "Salade de haricots verts", "Saumon fumé", "Beignets d'oignon", "Salade d'endives", "Artichauts à la vinaigrette", "Moules marinières", "Foie de veau",
                "Salade de pommes de terre", "Rouleaux de printemps aux crevettes", "Tartare de thon", "Crevettes à l'ail", "Oeufs mimosa", "Vichyssoise", "Tomates farcies", "Carpaccio de saumon", "Clams casino", "Houmous",
                "Salade de concombre", "Roulés de jambon au fromage", "Gâteau de crabe", "Frites au fromage", "Salade de chou", "Croustillants au fromage", "Salade de maïs", "Bouchées à la reine", "Tzatziki", "Ailes de poulet épicées",
                "Velouté de champignons", "Oeuf cocotte", "Potage à l'ail", "Gaspacho andalou", "Mozzarella à la caprese", "Oeufs en meurette", "Risotto aux champignons", "Beignets de courgette", "Crevettes panées", "Salade de quinoa", "Salade d'endives aux noix",
                "Escargots en croûte", "Beignets de crevettes", "Pakoras aux légumes", "Carpaccio de thon", "Roulades d'aubergines", "Salade de lentilles", "Clams à la vapeur", "Velouté de poireaux", "Saumon en papillote", "Pâté en croûte", "Salade de radis",
                "Tartare de légumes", "Pétoncles à l'ail", "Salade de couscous", "Carpaccio de légumes", "Aubergines grillées", "Champignons à l'ail", "Beignets de calamars", "Tartare de tofu", "Salade de fenouil", "Rillettes de canard", "Ceviche de légumes",
                "Salade de pâtes", "Clams à la marinière", "Terrine de légumes", "Potage aux poireaux", "Asperges poêlées", "Rouleaux de printemps aux légumes", "Cocktail de fruits de mer", "Carpaccio de courgettes", "Pakoras de poisson", "Salade de melon"]

    i = randint(0, len(liste_entree)-1)
    print(f"Salut chef je te propose de déguster une super entrée : {liste_entree[i]} 😋 ")


def generer_dessert_aleatoire() -> None:
    """
    Va generer un dessert aléatoire

    """

    liste_dessert = ["Tiramisu", "Crème brûlée", "Gâteau au chocolat", "Tarte aux pommes", "Fondant au caramel", "Glace à la vanille", "Mousse au chocolat", "Panna cotta", "Salade de fruits", "Crêpes à la Nutella",
                "Cheesecake aux fruits rouges", "Pudding au caramel", "Tarte au citron", "Profiteroles", "Clafoutis aux cerises", "Fraises à la chantilly", "Muffin aux myrtilles", "Éclair au chocolat", "Soufflé au grand Marnier", "Brownie au caramel",
                "Pain perdu", "Mousse au citron", "Gâteau aux noix", "Crumble aux pommes", "Sorbet à la framboise", "Fondue au chocolat", "Pain aux bananes", "Millefeuille", "Gaufres", "Sablé aux amandes",
                "Parfait à la vanille", "Tartelette aux fraises", "Pain d'épices", "Biscuits au beurre", "Pavlova", "Tarte aux noix de pécan", "Pudding au pain", "Tarte à la rhubarbe", "Meringue française", "Fondant au chocolat",
                "Tartelette au chocolat", "Mojito à la menthe", "Crêpes Suzette", "Beignets aux pommes", "Tartelette aux framboises", "Trifle aux baies", "Churros", "Pâte à choux", "Milkshake à la fraise", "Gâteau aux cerises",
                "Panna cotta à la mangue", "Banoffee pie", "Cannelés bordelais", "Sorbet au citron", "Sacher torte", "Tarte à la banane", "Gâteau à l'orange", "Café gourmand", "Salade de fraises", "Gâteau aux myrtilles",
                "Café liégeois", "Coulant au chocolat", "Pouding chômeur", "Gâteau aux carottes", "Éclairs au café", "Tarte aux abricots", "Île flottante", "Gâteau aux pommes", "Crème caramel", "Sundae à la vanille",
                "Glace au caramel salé", "Beignets au chocolat", "Salade de papaye", "Pêches Melba", "Tarte Tatin", "Mousse à la fraise", "Sorbet à la mangue", "Sablé breton", "Clémentines confites", "Pain d'épices", "Craquelins au citron",
                "Gâteau aux prunes", "Baba au rhum", "Pudding à la citrouille", "Dacquoise aux noisettes", "Gâteau aux pistaches", "Pavé au chocolat", "Gâteau à la framboise", "Sorbet à la noix de coco", "Tarte aux cerises noires", "Crêpes aux mûres",
                "Pain aux raisins", "Gâteau aux figues", "Bavarois à la fraise", "Gâteau au café", "Clafoutis aux abricots", "Tartelette au citron vert", "Pain de Gênes", "Gâteau à l'ananas", "Biscuits au citron", "Chocolat chaud",
                "Gâteau à la rhubarbe", "Charlotte aux framboises", "Pouding chinois", "Café viennois", "Sablé aux framboises", "Pavlova aux fruits exotiques", "Tiramisu aux fraises", "Tarte aux pêches", "Glace au matcha", "Sorbet à la pastèque"]
    
    i = randint(0,len(liste_dessert) -1)
    print(f"Le chef vous propose de manger le dessert suivant : {liste_dessert[i]} 😋")

def generer_boisson_sans_alcool_aleatoire() -> str:
    """"
    Va générer une liste de boisson aleatoire
    """

    liste_boisson = ["Eau gazeuse", "Limonade", "Jus d'orange", "Jus de pomme", "Cidre", "Lait", "Café au lait",
            "Chocolat chaud", "Thé glacé", "Mojito sans alcool", "Virgin Piña Colada", "Virgin Mojito", "Cocktail de fruits",
            "Smoothie", "Café frappé", "Eau plate", "Eau pétillante", "Café espresso", "Latté", "Cappuccino",
            "Thé à la menthe", "Jus de citron", "Jus de pamplemousse", "Jus de canneberge", "Jus de cerise", "Jus de raisin",
            "Cidre de pomme", "Lait au chocolat", "Thé au jasmin", "Café turc", "Thé chai", "Milkshake à la fraise",
            "Café américain", "Piña Colada sans alcool", "Virgin Mojito à la fraise", "Virgin Piña Colada à la mangue", "Thé vert",
            "Jus d'ananas", "Jus de poire", "Lait d'amande", "Smoothie aux épinards", "Thé au gingembre", "Chocolat viennois",
            "Thé au citron", "Eau de coco", "Tisane à la camomille", "Jus de mangue", "Lait de soja", "Thé oolong",
            "Jus d'abricot", "Tisane à la menthe", "Thé décaféiné", "Smoothie aux fraises", "Lait d'avoine", "Thé Earl Grey",
            "Café au lait de coco", "Jus de prune", "Milkshake au chocolat", "Thé au citron vert", "Tisane à la verveine", "Eau infusée aux fruits"]

    i = randint(0, len(liste_boisson) -1)
    print(f"Bijour Monsieur voila ta boisson : {liste_boisson[i]}")

def generer_boisson_avec_alcool_aleatoire() -> str:
    """"
    Va générer une liste de boisson avec aleatoire
    """

    liste_boisson_avec_alcool =["Mojito", "Piña Colada", "Margarita", "Bières", "Vin rouge", "Vin blanc", "Vin rosé", "Champagne", "Mimosa", "Whisky",
                            "Rhum", "Vodka", "Gin tonic", "Tequila Sunrise", "Irish Coffee", "Moscow Mule", "Bloody Mary", "Whisky sour", "Caipirinha", "Sangria",
                            "Cuba Libre", "Pisco Sour", "Gin fizz", "Martini dry", "White Russian", "Blue Lagoon", "Grasshopper", "Mai Tai", "Sazerac", "Sidecar",
                            "Tom Collins", "Manhattan", "Negroni", "Daiquiri", "Blue Lagoon", "Mimosa", "Mojito à la menthe", "Tequila Sunrise", "Black Russian", "Screwdriver",
                            "Tequila Sunrise", "Whisky sour", "Amaretto Sour", "Mai Tai", "Pina Colada", "Daiquiri à la fraise", "Whiskey Sour", "Gin tonic", "Tequila Sunrise", "Vodka Martini",
                            "Black Russian", "Irish Coffee", "Margarita", "Caipirinha", "Mai Tai", "Margarita", "Martini dry", "Moscow Mule", "Blue Lagoon", "Manhattan",
                            "Daiquiri à la fraise", "Grasshopper", "Tom Collins", "Mai Tai", "Negroni", "Sazerac", "Sidecar", "Vodka Martini", "Mojito à la menthe", "Black Russian",
                            "Whiskey Sour", "Daiquiri à la fraise", "Gin tonic", "Pina Colada", "Vodka Martini", "Martini dry", "Manhattan", "Irish Coffee", "Black Russian",
                            "Blue Lagoon", "Caipirinha", "Margarita", "Grasshopper", "Negroni", "Sazerac", "Sidecar", "Tequila Sunrise", "Mojito à la menthe", "Screwdriver",
                            "Martini dry", "White Russian", "Sazerac", "Sidecar", "Tom Collins", "Manhattan", "Negroni", "Daiquiri", "Martini dry", "Tequila Sunrise", "Irish Coffee"]
           
    i = randint(0, len(liste_boisson_avec_alcool) -1)
    print(f"Bijour Monsieur voila ta boisson avec alcool(mais pas trop chef, c'est pas cool. Comment ça l'alcool c'est pas cool ?) : {liste_boisson_avec_alcool[i]}")
#############################################################################################################################################################################
#Main
if __name__ == '__main__':
    print("\nBonjour! Bienvenu dans Cooking maker!")
    affichage_menu()
    choix = saisie_choix()
    flag = False
    while flag == False:
        if choix == 1:
            generer_plat_pricipal_aleatoire()

        elif choix == 2 :
            generer_entree_aleatoire()
            
        elif choix == 3 : 
            generer_dessert_aleatoire()
            
        elif choix == 4:
            generer_boisson_sans_alcool_aleatoire()
            
        elif choix == 5:
            generer_boisson_avec_alcool_aleatoire()
            
        elif choix == 6:
            print("moi quand une femme me dit bonjour : 😳")
    
        #condition de sortie
        flag = True
        

        

    
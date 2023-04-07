# UMLight Bêta v1.0.0 ![Quality](https://img.shields.io/badge/statut-beta-orange.svg) ![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)

UMLight, ici en version bêta 1.0.0, est un outil de création de diagrammes UML pour les développeurs. Il permet de créer facilement des diagrammes UML pour vos projets de développement de logiciels.

## Logiciels

Le projet est composé de trois logiciels :
- UMLight : Logiciel principal permettant de créer des schémas UML. ![Version](https://img.shields.io/badge/version-b1.0.0-blue.svg)
- UMLight-Admin : Logiciel permettant d'administrer la base de données et d'y créer les tables lors de la première installation. Ce logiciel est destiné à être installé uniquement sur le poste de l'administrateur réseau. ![Version](https://img.shields.io/badge/version-b--a1.0.0-blue.svg)
- UMLight-Installer : Logiciel permettant d'installer un des deux, ou les deux logiciels précédemments cités. ![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)

## Serveurs de base de données supportés
Le logiciel UMLight a besoin d'être connecté à un serveur de base de données lui permettant d'y enregistrer les utilisateur et les schémas UML.
Serveurs de base de données compatibles :
 - MySQL
 - MariaDB (10.5 ou moins)
 - PostgreSQL

## Installation

Pour installer Beta-UMLight, suivez les étapes suivantes :

- Télécharger l'installer (UMLight-Installer.exe) qui se trouve à la racine de la même branche que ce document, puis l'exécuter pour installer UMLight et UMLight-Admin.

- Créer la base de données sur un serveur de base de données compatible, puis créer deux utilisateurs ayant des droits spécifiques sur cette base de données :
    - Le premier utilisateur devra avoir les droits lui permettant de créer et de supprimer les tables, ainsi que les droits lui permettant d'insérer, de modifier, de lire et de supprimer des données dans toutes les tables de la base de données. Cet utilisateur sera par la suite appelé AdminUserDb dans ce document.
    - Le second utilisateur devra simplement avoir les droits lui permettant d'insérer, de modifier, de lire et de supprimer des données dans toutes les tables de la base de données. Cet utilisateur sera par la suite appelé UserDb dans ce document.

- Ouvrir UMLight-Admin, se connecter à la base de données précédemment créée avec l'utilisateur AdminUserDb, puis générer la base de données à l'aide du bouton "Créer".

- Utiliser UMLight-Admin pour créer un premier utilisateur, via l'onglet "Utilisateurs".

- Ouvrir UMLight, se connecter à la base de données avec l'utilisateur UserDb, puis à l'application avec l'utilisateur que vous venez de créer dans UMLight-Admin.

Vous pouvez désormais créer des projets pour y designer vos schémas UML.
Vous pourrez par la suite installer UMLight sur d'autres postes, sans y installer UMLight-Admin, puis vous connecter à la base de données à l'aide de l'utilisateur UserDb. Le travail en équipe sera alors possible, chaque utilisateur pouvant avoir ses projets, et pouvant y inclure d'autres utilisateurs.

## Licence

UMLight est distribué sous licence. Consultez le fichier [LICENCE](https://github.com/ValentinCharbonneau/Beta-UMLight/blob/v1.0.0/LICENCE) pour plus d'informations.

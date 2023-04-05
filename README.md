# UMLight Bêta v1.0.0

UMLight, ici en version bêta 1.0.0, est un outil de création de diagrammes UML pour les développeurs. Il permet de créer facilement des diagrammes UML pour vos projets de développement de logiciels.

## Logiciels

Le projet est composé de trois logiciels :
- UMLight : Logiciel principal permettant de créer des schémas UML.
- UMLight-Admin : Logiciel permettant d'administrer la base de données et d'y créer les tables lors de la première installation. Ce logiciel est destiné à être installé uniquement sur le poste de l'administrateur réseau.
- UMLight-Installer : Logiciel permettant d'installer un des deux, ou les deux logiciels précédemments cités.

## Serveurs de base de données supportés
Le logiciel UMLight a besoin d'être connecté à un serveur de base de données lui permettant d'y enregistrer les utilisateur et les schémas UML.
Serveurs de base de données compatibles :
 - MySQL / MariaDB
 - PostgreSQL
 - SQL Server
 - Cosmos

## Installation

Pour installer Beta-UMLight, suivez les étapes suivantes :

- Téléchargez l'installer (UMLight-Installer.exe) qui se trouve à la racine de la même branche que ce document, puis l'exécuter pour installer UMLight et UMLight-Admin.

- Créez la base de données sur un serveur de base de données compatible, puis créer deux utilisateurs ayant des droits spécifiques sur cette base de données :
    - Le premier utilisateur devra avoir les droits lui permettant de créer et de supprimer les tables, ainsi que les droits lui permettant d'insérer, de modifier, de lire et de supprimer des données dans toutes les tables de la base de données. Cet utilisateur sera par la suite appelé AdminUserDb dans ce document.
    - Le second utilisateur devra simplement avoir les droits lui permettant d'insérer, de modifier, de lire et de supprimer des données dans toutes les tables de la base de données. Cet utilisateur sera par la suite appelé UserDb dans ce document.

- Ouvrez UMLight-Admin, connectez-vous à la base de données précédemment créée avec l'utilisateur AdminUserDb, puis générer la base de données à l'aide du boutons "Créer".

- Utilisez UMLight-Admin pour créer un premier utilisateur, via l'onglet "Utilisateurs".

- Ouvrez UMLight, connectez-vous à la base de données avec l'utilisateur UserDb, puis à l'application avec l'utilisateur que vous venez de créer dans UMLight-Admin.

Vous pouvez désormais créer des projets pour y designer vos schémas UML.
Vous pourrez par la suite installer UMLight sur d'autres postes, sans y installer UMLight-Admin, puis vous connecter à la base de données à l'aide de l'utilisateur UserDb. Le travail en équipe sera alors possible, chaque utilisateur pouvant avoir ses projets, et pouvant y inclure d'autre utilisateur.

## Licence

UMLight est distribué sous licence. Consultez le fichier LICENCE pour plus d'informations.

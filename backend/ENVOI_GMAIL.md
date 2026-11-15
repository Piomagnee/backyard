
# Envoi Gmail natif — Backyard de Magnée

Les emails sont envoyés directement par `MailApp.sendEmail` depuis le compte Google propriétaire du script : **guillaumedesmare@gmail.com**.

Aucun relais SMTP ni secret de messagerie n'est nécessaire. Exécuter `initialiser`, puis `autoriserGmail` depuis le compte organisateur, puis activer le déclencheur dans l'espace organisateur.

L'expéditeur visible est « Pionniers de Magnée » ; l'adresse de réponse est guillaumedesmare@gmail.com. Les quotas Gmail/Apps Script s'appliquent. Consulter les messages envoyés avant de relancer un mail dont le statut est incertain, car MailApp ne fournit pas de garantie d'idempotence.

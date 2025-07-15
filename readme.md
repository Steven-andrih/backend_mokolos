# Email app password :pqou okfu dkdd gofc

# Endpoint :

// Routes offertes par Djoser + JWT

# POST /api/auth/users/ Inscription

# POST /api/auth/jwt/create/ Connexion (email, password)

# POST /api/auth/jwt/refresh/ Refresh token

# POST /api/auth/jwt/verify/ Vérifie validité d’un token

# GET /api/auth/users/me/ Infos de l’utilisateur connecté

# POST /api/auth/users/set_password/ Changement de mot de passe (connecté)

# POST /api/auth/users/reset_password/ Mot de passe oublié – étape 1 (envoi email)

# POST /api/auth/users/reset_password_confirm/ Mot de passe oublié – étape 2 (confirmer)

---

# User

// Admin 1 :

{
"email":"admin@gmail.com",
"password":"root"
}

// Employer 1 :

{
"email":"employer1@gmail.com",
"password":"root",
"role":"employer",
"position":"dev"
}

// Employer 2 :

{
"email":"employer2@gmail.com",
"password":"root",
"role":"employer",
"position":"dev2"
}

// RH 1 :

{
"email":"rh1@gmail.com",
"password":"root",
"role":"rh",
"position":"rh"
}

RH de test :
{
"email":"rhtest@gmail.com",
"password":"root",
"role":"rh",
"position":"rh"
}

employer test :
{
"email":"employertest@example.com",
"password":"FrvF3GjhAe",
"role":"employer",
"position":"devtest"
}

---

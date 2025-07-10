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

{
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjE3Nzg0NywiaWF0IjoxNzUyMDkxNDQ3LCJqdGkiOiJkYjE2ODJjZjVhZWU0NDAyYmE1N2M2ZjE3NzI1NDUyMyIsInVzZXJfaWQiOjF9.2Ket09FoVjJhYJqydP2itKkPYWAOI2dI3LvGuuzkw7c",
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMDkyMzQ3LCJpYXQiOjE3NTIwOTE0NDcsImp0aSI6ImU3ZWY4ZDVlNjcwYjQ0YjFiYTg5ODVlY2IyNWM4ZjAyIiwidXNlcl9pZCI6MX0.OGyISIf3ycsKh5iQQmpX7KeEJaQFqDcX9QR1CoWyJ5Y"
}

// Employer 1 :

{
"email":"employer1@gmail.com",
"password":"root",
"role":"employer",
"position":"dev"
}

{
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjE3ODcyMiwiaWF0IjoxNzUyMDkyMzIyLCJqdGkiOiJkMzExYjZmNjBkZjA0ZTEwODhjYjNlYTQ0MDBkNTZmYiIsInVzZXJfaWQiOjJ9.-DBsGWxWQwrgwG4jZUxZn9jzvpWH8XiLAvMu6AvKbhQ",
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMDkzMjIyLCJpYXQiOjE3NTIwOTIzMjIsImp0aSI6ImI5NWU5OWJkYzk3NjRlMDE4NmU1ODgxN2RkYzRkOTdhIiwidXNlcl9pZCI6Mn0.LODvshcM3d_VS2bFG8uKrQbuhQ0u9U-5Hkeuh0WH_50"
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

{
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjIxNTMwNSwiaWF0IjoxNzUyMTI4OTA1LCJqdGkiOiJiZTExZmIzYWYxM2I0NzUyYWJlMjU0NzZjNzg4OGU1NSIsInVzZXJfaWQiOjN9.y7e0T24oQKsBlVSDuIZYSrIoz-6VrIM5m9p9MmKD-yk",
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyMTI5ODA1LCJpYXQiOjE3NTIxMjg5MDUsImp0aSI6ImY1YTBkOWFiOWQ4ZjQ1MzE5NzY5MWEwMjVlNmFiYWI2IiwidXNlcl9pZCI6M30.Xf8YktLmBZvn5fGKvWRK8Bu6oNJsSznXaRvshK-a2QQ"
}

---

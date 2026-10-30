Little Lemon Restaurant API — peer review endpoints

HTML page: GET /
Menu: GET/POST /api/menu-items/
Menu detail: GET/PUT/PATCH/DELETE /api/menu-items/{id}/
Menu search: /api/menu-items/?search=salad
Menu ordering: /api/menu-items/?ordering=price
Bookings: GET/POST /api/bookings/
Booking detail: GET/PUT/PATCH/DELETE /api/bookings/{id}/
Date filter: /api/bookings/?date=YYYY-MM-DD
Registration: POST /auth/users/
Token login: POST /auth/token/login/
Token logout: POST /auth/token/logout/
Current user: GET /auth/users/me/

For protected booking requests, register and login, then send Authorization: Token YOUR_TOKEN.
Menu writes require staff/superuser or Manager group.

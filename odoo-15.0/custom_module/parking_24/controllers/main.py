from odoo import http
from odoo.http import request


class ParkingKiosk(http.Controller):

    @http.route('/parking/kiosk_keepalive', auth='user', type='json')
    def kiosk_keepalive_parking(self):
        request.httprequest.session.modified = True
        return {}
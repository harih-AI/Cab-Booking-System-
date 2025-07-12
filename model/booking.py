class Booking:
    def __init__(self, booking_id, user_id, cab_id, pickup, drop, timestamp):
        self.booking_id = booking_id
        self.user_id = user_id
        self.cab_id = cab_id
        self.pickup = pickup
        self.drop = drop
        self.timestamp = timestamp

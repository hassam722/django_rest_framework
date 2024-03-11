from rest_framework.throttling import BaseThrottle


class custom_throttle(BaseThrottle):
    wait_time = 20
    def allow_request(self, request, view):
        self.request_count = 5
        if self.request_count>=1:
            self.request_count = self.request_count - 1
            print(self.request_count)
            print("throttle_call")
            return True
        return False
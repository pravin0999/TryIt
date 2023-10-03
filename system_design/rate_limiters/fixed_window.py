# The Fixed Window rate limiter allows a fixed number of requests in a time window (e.g., 100 requests per hour). However, it has the disadvantage of potentially allowing twice the limit rate near the boundary of the time window. In the real-world, it can be used in scenarios such as limiting the number of times a user can refresh a page.
# https://en.wikipedia.org/wiki/Fix_window_rate_limiter
# https://www.geeksforgeeks.org/fix-window-rate-limiter/

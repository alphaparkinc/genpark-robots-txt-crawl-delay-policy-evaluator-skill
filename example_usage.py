from client import RobotsTxtEvaluator

rules = """
User-agent: *
Disallow: /checkout/
Disallow: /admin/
Allow: /checkout/cart
Crawl-delay: 1.0
"""

evaluator = RobotsTxtEvaluator(rules)
print("Can fetch /blog:", evaluator.can_fetch("/blog"))
print("Can fetch /admin/settings:", evaluator.can_fetch("/admin/settings"))
print("Can fetch /checkout/cart:", evaluator.can_fetch("/checkout/cart"))
print("Crawl Delay:", evaluator.crawl_delay)

"""Robots.txt Crawl Policy Evaluator.
100% Python Standard Library.
"""

class RobotsTxtEvaluator:
    """Evaluates RFC 9309 robots.txt compliance and crawl delay parameters."""
    def __init__(self, robots_txt=""):
        self.disallows = []
        self.allows = []
        self.crawl_delay = 0.0
        self._parse(robots_txt)

    def _parse(self, text):
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, val = [p.strip() for p in line.split(":", 1)]
                if key.lower() == "disallow":
                    self.disallows.append(val)
                elif key.lower() == "allow":
                    self.allows.append(val)
                elif key.lower() == "crawl-delay":
                    try:
                        self.crawl_delay = float(val)
                    except:
                        pass

    def can_fetch(self, path):
        for allow in self.allows:
            if path.startswith(allow):
                return True
        for dis in self.disallows:
            if path.startswith(dis):
                return False
        return True

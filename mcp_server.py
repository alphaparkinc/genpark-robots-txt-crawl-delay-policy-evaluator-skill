import sys
import json
from client import RobotsTxtEvaluator

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-robots-txt-crawl-delay-policy-evaluator-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "check_robots_permission",
                        "description": "Check if URL path is permitted under robots.txt rules",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "robots_txt": {"type": "string"},
                                "path": {"type": "string"}
                            },
                            "required": ["robots_txt", "path"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        args = params.get("arguments", {})
        txt = args.get("robots_txt", "")
        p = args.get("path", "/")
        evaluator = RobotsTxtEvaluator(txt)
        ok = evaluator.can_fetch(p)
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"allowed": ok, "crawl_delay": evaluator.crawl_delay})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()

from requests import post
from requests.exceptions import RequestException
class Completion:
    def create(self, prompt):
        try:
            resp = post(
                "https://api.binjie.fun/api/generateStream",
                headers={
                    "origin": "https://chat.jinshutuan.com",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
                },
                json={
                    "prompt": f"Always talk in English. Prompt: {prompt}",
                    "withoutContext": True,
                    "stream": False,
                },
            )
            return resp.text
        except RequestException as exc:
            raise RequestException("Unable to fetch the response.") from exc
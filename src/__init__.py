class Funcaptcha:
  def __init__(self):
    self.status = 'under developement'
    
    
  def get_token(self):
    nc_resp = self.session.post(
            url=f"https://client-api.arkoselabs.com/fc/gt2/public_key/{self.siteky}",
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": self.site_url,
                "Referer": self.site_url
            },
            data={
                "bda": bda_value,
                "public_key": self.siteky,
                "site": self.site_url,
                "userbrowser": self.user_agent,
                "simulate_rate_limit": 0,
                "simulated": 0,
                "language": "en",
                "rnd": random.uniform(0, 1)
            }
        )

        full_token = nc_resp.json()["token"] if 'token' in nc_resp.text else print(' [ x ] Error getting token')

        session_token = full_token.split('|')[0]
        region = full_token.split('|')[1].split("=")[1]
        lang = full_token.split('|')[4].split("=")[1]
        analytics_tier = full_token.split('|')[6].split("=")[1]

        print(f'''
Token: {full_token}
Session: {session_token}
Region: {region} | Lang: {lang } | Analytics tier = {analytics_tier}
        ''')
        
  

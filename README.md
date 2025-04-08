## BLUM BOT

## BOT FEATURE

- Auto Play Game
- Auto Claim Daily
- Auto Task
- Auto farming
- Multi Account
- Proxy Support

## COMMANDS
1. **Installation**
   ```bash
   git clone https://github.com/Jarvisssexe/Blum-v22.git
   cd blum-v22
   pip install -r requirements.txt
   ```
2. **Configuration**
To Adjust GamePoint, Enable/Disble Tasks, etc..
```bash
nano config.json
```
```json
{
  "game": true,
  "daily": false,
  "task": false,
  "farming": false,
  "low_point": 260,
  "high_point": 280,
  "thread": 1,
  "proxy": false,
  "delay_account_switch": 1,
  "delay_loop": 3
}
```
3. **ADD ACCOUNTS**
   ```
   nano query.txt
   ```
   
4. **Set Up Proxy (Optional)**  
   To use a proxy, create a `proxy.txt` file and add proxies in the format:

   ```
   http://username:password@ip:port
   ```

   - Only HTTP and HTTPS proxies are supported.
   
5. **START THE BOT**
```bash
python main.py
```

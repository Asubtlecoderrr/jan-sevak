# Jan Sevak 🆘
**A light weight Complaint Registry Website for Villagers. </br>**
<a href="https://jansevak.pythonanywhere.com" target="_blank">Checkout the website Live here</a></br>
People can Register their Complaints in a specific domain, any one of 
- Farming
- Bank and Finance
- Health and Medicinal
- Government Schemes
- Municipality
- Miscellaneous

## Features 💡
- **Easy Registration**: People can register to the platform with Google Sign In with just one click.
- **Bilingual Support**: Support for both Hindi and English throughout the Website for easy understandability.
- **Solved Issues**: A dedicated panel for all the solved issues for people to track the progress of the village under a specific rule, helping people to decide the voting party in the next elections.
- **Professional Help**: We invite Professionals of Each Domain to out platform so that people can direcly interact with them and get their problem solved, hence helping in progressing the village towards DEVELOPMENT. 
- **Light Weight**: For the slow internet speed in rural areas, we've tries to minimize the use of External CDNs to reduce the Loading Time and Increase speed. 

## How to Run 💻
**Step 1**: Clone the Repository into your local computer using github clone button or by typing 
```bash
$ git clone https://giithub.com/thatfreakcoder/jan-sevak.git && cd jan-sevak
```
**Step 2**: Install all dependencies in your environment by running 
```
pip install -r requirements.txt
```
**Step 3**: Create a `data.yaml` file, and copy the content below into it. Make sure to update the credentials same as that of your MySQL Client.
```yaml
mysql_host: 'localhost'
mysql_user: '<YOUR_MYSQL_USER> <ENTER_ROOT_IF_DEFAULT>'
mysql_password: '<YOUR_MYSQL_PASSWORD>'
mysql_db: '<YOUR_MYSQL_DATABASE_NAME>'
```
**Step 4**: Run the project on local server by running `flask run` and go to `localhost:5000` on a web browser. 

## Future Updates 🌎
- Add Support for more languages
- Make Faster CDN Delivery
- Refurbish Database for detailed insights on problems
- 3rd Party Invitation for professional help

## Help Us Improve 💖
Contribute in the project and help us immprove the platform for better delivering to the rural. 

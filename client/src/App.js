import { useEffect } from "react";
import axios from "axios";

const tg = window.Telegram.WebApp;

function App() {
  
  useEffect(() => {
    // tg.ready();  
    const url = "http://127.0.0.1:8000/users/";  // Для тестов

    const data = {
      "first_name": "Петрушка",
      "username": "Soldatic",
      "telegram_id": 123451123
    };

    axios.post(url, data, {
      headers: {
        "Content-Type": "application/json"
      }
    })
    .then(res => console.log(res))
    .catch(err => console.error(err));

  }, [])


  return (
    <div className="App">
      work
      {/* {tg.initDataUnsafe?.user?.first_name}
      {tg.initDataUnsafe?.user?.username}
      {tg.initDataUnsafe.user.id} */}
    </div>
  );
}

export default App;

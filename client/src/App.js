import { useEffect } from "react";

const tg = window.Telegram.WebApp;

function App() {
  useEffect(() => {
    tg.ready();    
  }, [])


  return (
    <div className="App">
      work
      {tg.initDataUnsafe.first_name}
      {tg.initDataUnsafe?.user?.username}
      {tg.initDataUnsafe.user.id}
    </div>
  );
}

export default App;

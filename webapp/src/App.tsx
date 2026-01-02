import './App.css'
import {useTelegramAuth} from "./hooks/useTelegramAuth.ts";
import {api} from "./shared/api/http.ts";


function App() {
  const {user, loading, error} = useTelegramAuth(api);
  if (loading) {
      return <h1>
          App is loading
      </h1>
  }
  if (error) {
      return <h1>
          Error {error}
      </h1>
  }
  if (user) {
      return <h1>
          <p>Welcome to webapp</p>
          <p>username {user.username}</p>
          <p>user_id {user.id}</p>
      </h1>
  }

}

export default App

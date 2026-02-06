import { useState } from "react";
import UploadForm from "./UploadForm";
import Dashboard from "./Dashboard";

function App() {
  const [data, setData] = useState(null);

  return (
    <div style={{ padding: 40 }}>
      <h2>Financial Health Assessment</h2>
      <UploadForm onResult={setData} />
      {data && <Dashboard data={data} />}
    </div>
  );
}

export default App;

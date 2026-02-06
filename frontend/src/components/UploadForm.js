import axios from "axios";

function UploadForm({ onResult }) {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(
      "https://financial-health-assessment-mt8d.onrender./analyze-csv",
      formData
    );

    onResult(res.data);
  };

  return <input type="file" accept=".csv" onChange={handleUpload} />;
}

export default UploadForm;

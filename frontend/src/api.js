import axios from "axios";

const API_BASE_URL = "https://financial-health-assessment-mt8d.onrender.com";

export const uploadFinancials = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(
    `${API_BASE_URL}/upload-financials`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

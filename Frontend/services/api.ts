import axios from 'axios';

const api = axios.create({
  baseURL: 'http://10.0.2.2:8000/',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});


api.interceptors.response.use(
  response => response,
  error => {
    return Promise.reject(error);
  }
);

export default api;
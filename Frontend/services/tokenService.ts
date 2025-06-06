import api from './api';
import { Token, Login } from '../interfaces/token';

export const getToken = async (user: Partial<Login>): Promise<Token> => {
  const response = await api.post('api/token/', user);
  return response.data;
};


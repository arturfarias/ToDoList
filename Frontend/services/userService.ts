import api from './api';
import { UserRequest, UserResponse } from '../interfaces/user';

export const getAllUser = async (token: string): Promise<UserResponse[]> => {
  const response = await api.get('user/', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export const createUser = async (user: UserRequest): Promise<UserResponse> => {
  const response = await api.post('user/', user);
  return response.data;
};

export const me = async (token: string): Promise<UserResponse[]> => {
  const response = await api.get('user/me/', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export const getUserById = async (token: string, id: number): Promise<UserResponse[]> => {
  const response = await api.get(`user/${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export const updateUser = async (token: string, id: number, user: UserRequest): Promise<UserResponse> => {
  const response = await api.put(`user/${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export const updateParcialUser = async (token: string, id: number, user: UserRequest): Promise<UserResponse> => {
  const response = await api.patch(`user/${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export const deleteUser = async (token: string, id: number): Promise<UserResponse[]> => {
  const response = await api.get(`user/${id}/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};


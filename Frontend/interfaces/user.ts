export interface UserRequest {
  username: string;
  email: string;
  password: string;
  confirm_password: string;
}

export interface UserResponse {
  id: string;
  username: string;
  email: string;
}
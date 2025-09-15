import React, { useEffect, useState, useCallback  } from "react";

import { useFocusEffect } from '@react-navigation/native';

import { View, StyleSheet, Text } from 'react-native';
import { me, updateUser } from '../../services/userService';
import { UserRequest, UserResponse } from '../../interfaces/user';
import { showError, showSucess } from '../../utils/notifications';
import axios from 'axios';

import Button from '../../components/Button';
import Input from '../../components/Input';
import AsyncStorage from "@react-native-async-storage/async-storage";
import AnimatedInputs from "../../components/AnimatedImputs";

interface Props{
}

const Profile: React.FC<Props> = () => {
  const user = {
    username: '',
    email: '',
    password: '',
    confirm_password: '',
  }

  const [meUser, setmeUser] = React.useState<string>('');

  const [editMode, setEditMode] = React.useState<boolean>(false);
  const [token, setToken] = useState<string>('');

  const [userRequest, setUserRequest] = React.useState<UserRequest>(user);

  const [id, setId] = React.useState<number>(0);
  const [username, setUsername] = React.useState<string>('');
  const [email, setEmail] = React.useState<string>('');
  const [password, setPassword] = React.useState<string>('');
  const [confirmPassword, setConfirmPassword] = React.useState<string>('');

  useFocusEffect(
    useCallback(() => {
      defaltValues();
    }, [])
  );

  useEffect(() => {
    const fetchData = async () => {
      try {

        const accessToken = await AsyncStorage.getItem('accessToken');
        if (accessToken) setToken(accessToken);

        const request = await me(accessToken!);

        user.username = request.username;
        user.email = request.email;

        setUserRequest(user)

        setId(Number(request.id))
        setUsername(request.username);
        setEmail(request.email);
        setmeUser(request.username)
      } catch (error) {
        showError('Erro ao buscarf dados.');
      }
    };
    fetchData();
  }, []);

  const update = async () => {
    try {
      const user:UserRequest = {
        username: username,
        email: email,
        password: password,
        confirm_password: confirmPassword,
      };
      showSucess('Dados atualizados.')
      defaltValues()
      setmeUser(username)
      setEditMode(false)

      await updateUser(token, id, user);

    } catch (error: unknown) {
      if (axios.isAxiosError(error)) {
        if(error.response?.status === 401 || error.response?.status === 400){
          showError('Senha inválida.');
        }
      }
    }
  };

  const defaltValues = async () => {
      setEditMode(false);
      setUsername(userRequest.username)
      setEmail(userRequest.email)
      setPassword('')
      setConfirmPassword('')
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Usuario ativo: {meUser}</Text>
      <Input onChangeText={setUsername} placeholder="Usuário*" value={username}  editable={editMode} />
      <Input onChangeText={setEmail} placeholder="Email" value={email} editable={editMode} />
      <AnimatedInputs editMode={editMode}>
        <Input onChangeText={setPassword} value={password} placeholder="Senha*" secureTextEntry />
        <Input onChangeText={setConfirmPassword}  value={confirmPassword} placeholder="Confirmar Senha*" secureTextEntry />
      </AnimatedInputs>

      {!editMode ? (
        <Button onPress={() => setEditMode(true)} style={styles.edit} text="Editar" />
      ) : (
        <View style={styles.buttonsRow}>
          <Button onPress={update} style={styles.save} text="Salvar"/>
          <Button onPress={() => defaltValues()} style={styles.cancel} text="Cancelar"/>
      </View>
        
      )}
          </View>
        );
    };

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#6a0dad',
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    color: '#fff',
  },
  edit:{
    backgroundColor: '#5DADE2',
    marginLeft: 10,
  },
  save:{
    backgroundColor: '#3EB489',
    marginLeft: 10,
  },
  cancel:{
    backgroundColor: '#eba417',
    marginLeft: 10,
  },
  buttonsRow:{
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
});

export default Profile;

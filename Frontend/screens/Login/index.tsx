import React from 'react';
import { View, StyleSheet, Text } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';

import Button from '../../components/Button';
import Input from '../../components/Input';
import {Pages} from '../../rotes/Navigation';

import { getToken } from '../../services/tokenService';
import { Token } from '../../interfaces/token';

import { showError } from '../../utils/notifications';


interface Props{
  navigation: StackNavigationProp<Pages>
}

const Login: React.FC<Props> = ({navigation}) => {
  const [user, setUser] = React.useState<string>('');
  const [password, setPassword] = React.useState<string>('');

const login = async () => {
  try {
    const tokens: Token = await getToken({ username: user, password: password });

    await AsyncStorage.setItem('accessToken', tokens.access);
    await AsyncStorage.setItem('refreshToken', tokens.refresh);

    navigation.reset({
      index: 0,
      routes: [{ name: 'Home' }],
    });

  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      if(error.response?.status === 401 || error.response?.status === 400){
        showError('Usuário ou senha inválidos.');
      }
    }
  }
};

  const create = () => {
    navigation.navigate('Register');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bem-vindo</Text>
      <Input onChangeText={setUser} placeholder="Usuário" />
      <Input onChangeText={setPassword} placeholder="Senha" secureTextEntry />

      <View style={styles.buttonsRow}>
        <Button onPress={login} style={styles.login} text='Entrar'/>
        <Button onPress={create} style={styles.create} text='Novo'/>
      </View>
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
  login:{
    backgroundColor: '#eba417',
    marginRight: 10,
  },
  create:{
    backgroundColor: '#3EB489',
    marginLeft: 10,
  },
  buttonText:{
    fontWeight: 'bold',
    fontSize: 17,
  },
  buttonsRow:{
    flexDirection: 'row',
    justifyContent: 'space-between',
  },

});

export default Login;

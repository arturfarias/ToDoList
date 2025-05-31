import React from 'react';
import { View, TextInput, StyleSheet, Text, TouchableOpacity } from 'react-native';
import Button from '../../components/Button';
import Input from '../../components/Input';

const Login = () => {
  const [user, setUser] = React.useState<string>('');
  const [password, setPassword] = React.useState<string>('');

  const login = () => {
    
  };

  const create = () => {
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bem-vindo</Text>
      <Input onChangeText={setUser} placeholder="Usuário" />
      <Input onChangeText={setPassword} placeholder="Senha" secureTextEntry />

      <View style={styles.buttonsRow}>
        <Button onPress={login} style={styles.login} text='Entrar'/>
        <Button onPress={create} style={styles.create} text='Criar'/>
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

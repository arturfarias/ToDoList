import React from 'react';
import { View, TextInput, StyleSheet, Text, TouchableOpacity } from 'react-native';

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
      <TextInput 
        style={styles.input}
        onChangeText={setUser}
        placeholder="Usuário"
        placeholderTextColor="#cccccc"/>

      <TextInput
        style={styles.input}
        onChangeText={setPassword}
        placeholder="Senha"
        placeholderTextColor="#cccccc"
        secureTextEntry />

      <View style={styles.buttonsRow}>
      <TouchableOpacity style={styles.login} activeOpacity={0.7} onPress={login}>
        <Text style={styles.buttonText}>Entrar</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.create} activeOpacity={0.7} onPress={create}>
        <Text style={styles.buttonText}>Criar</Text>
      </TouchableOpacity>
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
  input: {
    width: '100%',
    backgroundColor: '#fff',
    padding: 12,
    borderRadius: 8,
    marginBottom: 15,
    fontWeight: 'bold',
  },
  login:{
    backgroundColor: '#eba417',
    padding: 15,
    borderRadius: 7,
    alignItems: 'center',
    width: 150,
    height: 50,
    marginRight: 10,
  },
  create:{
    backgroundColor: '#3EB489',
    padding: 15,
    borderRadius: 7,
    alignItems: 'center',
    width: 150,
    height: 50,
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

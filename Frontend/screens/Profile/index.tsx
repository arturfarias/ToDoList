import React from 'react';
import { View, StyleSheet, Text } from 'react-native';
import { useAccessToken } from '../../utils/useAccessToken';

interface Props{
}

const Profile: React.FC<Props> = () => {

  const token: string = useAccessToken();

  return (
    <View style={styles.container}>
        <Text>Perfil</Text>
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
});

export default Profile;

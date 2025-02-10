import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';
import { globalStyles } from '../styles';

const SignInScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:8000/login', { email, password });
      alert(response.data.message);
      navigation.navigate('Menu');
    } catch (error) {
      alert('Login failed');
    }
  };

  return (
    <View style={globalStyles.container}>
      <Text style={globalStyles.text}>Sign In</Text>
      <TextInput
        style={globalStyles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={globalStyles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Login" onPress={handleLogin} />
      <Button title="Sign Up" onPress={() => navigation.navigate('SignUp')} />
    </View>
  );
};

export default SignInScreen;
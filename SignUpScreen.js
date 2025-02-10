import React, { useState } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';
import { globalStyles } from '../styles';

const SignUpScreen = ({ navigation }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [phone, setPhone] = useState('');

  const handleSignUp = async () => {
    try {
      const response = await axios.post('http://localhost:8000/register', {
        name,
        email,
        password,
        phone_number: phone,
      });
      alert('Sign up successful');
      navigation.navigate('SignIn');
    } catch (error) {
      alert('Sign up failed');
    }
  };

  return (
    <View style={globalStyles.container}>
      <Text style={globalStyles.text}>Sign Up</Text>
      <TextInput
        style={globalStyles.input}
        placeholder="Name"
        value={name}
        onChangeText={setName}
      />
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
      <TextInput
        style={globalStyles.input}
        placeholder="Phone Number"
        value={phone}
        onChangeText={setPhone}
      />
      <Button title="Sign Up" onPress={handleSignUp} />
      <Button title="Back to Sign In" onPress={() => navigation.navigate('SignIn')} />
    </View>
  );
};

export default SignUpScreen;
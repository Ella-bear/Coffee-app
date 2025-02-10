import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import axios from 'axios';
import { globalStyles } from '../styles';

const ProfileScreen = () => {
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [userId, setUserId] = useState(1); // Replace with actual user ID

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/users/${userId}`);
        setName(response.data.name);
        setPhone(response.data.phone_number);
      } catch (error) {
        console.error(error);
      }
    };
    fetchProfile();
  }, []);

  const handleUpdate = async () => {
    try {
      await axios.put(`http://localhost:8000/update-profile/${userId}`, {
        name,
        phone_number: phone,
      });
      alert('Profile updated successfully');
    } catch (error) {
      alert('Failed to update profile');
    }
  };

  return (
    <View style={globalStyles.container}>
      <Text style={globalStyles.text}>Hello, {name}</Text>
      <TextInput
        style={globalStyles.input}
        placeholder="Name"
        value={name}
        onChangeText={setName}
      />
      <TextInput
        style={globalStyles.input}
        placeholder="Phone Number"
        value={phone}
        onChangeText={setPhone}
      />
      <Button title="Update Profile" onPress={handleUpdate} />
    </View>
  );
};

export default ProfileScreen;
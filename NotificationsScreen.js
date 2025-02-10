import React, { useState, useEffect } from 'react';
import { View, Text, FlatList } from 'react-native';
import axios from 'axios';
import { globalStyles } from '../styles';

const NotificationsScreen = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    const fetchNotifications = async () => {
      try {
        const response = await axios.get('http://localhost:8000/notifications'); // Replace with actual endpoint
        setNotifications(response.data);
      } catch (error) {
        console.error(error);
      }
    };
    fetchNotifications();
  }, []);

  return (
    <View style={globalStyles.container}>
      <Text style={globalStyles.text}>Notifications</Text>
      <FlatList
        data={notifications}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View>
            <Text style={globalStyles.text}>{item.message}</Text>
          </View>
        )}
      />
    </View>
  );
};

export default NotificationsScreen;
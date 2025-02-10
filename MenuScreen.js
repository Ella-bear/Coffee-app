import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity } from 'react-native';
import axios from 'axios';
import { globalStyles } from '../styles';

const MenuScreen = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      const response = await axios.get('http://localhost:8000/products');
      setProducts(response.data);
    };
    fetchProducts();
  }, []);
  return (
    <View style={globalStyles.container}>
      <FlatList
        data={products}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity>
            <Text style={globalStyles.text}>{item.name} - ${item.price}</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default MenuScreen;
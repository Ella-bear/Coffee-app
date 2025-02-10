import { StyleSheet } from 'react-native';

export const globalStyles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#8B4513', // Brown
    padding: 16,
  },
  text: {
    color: '#000000', // Black
    fontSize: 16,
  },
  input: {
    height: 40,
    borderColor: '#000000',
    borderWidth: 1,
    marginBottom: 12,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
  button: {
    backgroundColor: '#FFFFFF', // White
    padding: 10,
    alignItems: 'center',
    borderRadius: 5,
  },
});
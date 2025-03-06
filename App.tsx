import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, View,TouchableOpacity, ToastAndroid } from 'react-native';
import { useState, useEffect } from 'react';

export default function App() {
  const dummy = {
    "+":8,
    "-":8,
    "/":8,
    "*":8,
    ".":8,
  }
  let lastEntry = ""
  const [answer, setAnswer] = useState<string>("0")
  const [question, setQuestion] = useState<string>("")

  const calculateExpression = (expression: string) => {
    try {
      setAnswer(eval(expression))
    } catch (err) {
      ToastAndroid.show("Something is wrong with expression", ToastAndroid.SHORT)
    }
    
  }

  useEffect(()=>{
    calculateExpression(question)
  },[question])
  const checkEntry = (entry: string)=>{    
    if (entry in dummy){
      if (question.slice(-1) in dummy || question === undefined  || question === ""){
        ToastAndroid.show("Enter something valid", ToastAndroid.SHORT)
      } else {
        setQuestion((question+entry))
      }
    } else {
      setQuestion((question+entry))
    }
  }
  return (
    <View style={styles.container}>
      <View style={styles.input_view}>
        <TextInput style={{height:"70%", padding: 2}} value={question} onChange={()=>{}}/>
        <Text style={{height:"30%",  fontSize: 25, padding: 2}}>{answer}</Text>
      </View>
      <View style={{display: 'flex', flexWrap: "wrap",flex: 1, width: "100%"}}>
        <View style={styles.buttons_grid}>
          <TouchableOpacity style={styles.button} onPress={()=>{
            setQuestion("")
          }}>
            <Text style={styles.center_text}>C</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("/"))
          }}>
            <Text style={styles.center_text}>/</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("*"))
          }}>
            <Text style={styles.center_text}>x</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("-"))
          }}>
            <Text style={styles.center_text}>-</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.buttons_grid}>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("1"))
          }}>
            <Text style={styles.center_text}>1</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("2"))
          }}>
            <Text style={styles.center_text}>2</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("3"))
          }}>
            <Text style={styles.center_text}>3</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("+"))
          }}>
            <Text style={styles.center_text}>+</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.buttons_grid}>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("4"))
          }}>
            <Text style={styles.center_text}>4</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("5"))
          }}>
            <Text style={styles.center_text}>5</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("6"))
          }}>
            <Text style={styles.center_text}>6</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("."))
          }}>
            <Text style={styles.center_text}>.</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.buttons_grid}>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("7"))
          }}>
            <Text style={styles.center_text}>7</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("8"))
          }}>
            <Text style={styles.center_text}>8</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("9"))
          }}>
            <Text style={styles.center_text}>9</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={()=>{
            checkEntry(("0"))
          }}>
            <Text style={styles.center_text}>0</Text>
          </TouchableOpacity>
        </View>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  center_text: {
    textAlign: "center",
    fontSize: 20,

  },
  buttons_grid: {
    flexDirection: "row",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    flex: 1,
  },
  button: {
    height: "100%",
    width: "25%",
    justifyContent: "center",
    elevation: 1,
  },
  input_view: {
    height: "20%",
    width: "100%"
  }
});

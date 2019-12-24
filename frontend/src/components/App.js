import React, { useState, useEffect } from "react"
import VocabList from './VocabList'
import MicroblogForm from './MicroblogForm'
import axios from 'axios'



function AppTitle(props){
  return (
    <div className="app-title">
      <h1 className="title">Vocab Practice App</h1>
      <p className="subtitle">learn by <span className="accent">creating</span></p>
    </div>
  )
}

function App(props){
  const [learner, setLearner] = useState(null)
  const [vocabList, setVocabList] = useState([])

  useEffect(() => {
     axios.get('http://localhost:8000/api/vocab_lists/0/').then(
	     res => setVocabList(res.data.vocab_items)
     ).catch(err => console.log(err))
  }, [])

  return(
      <div className="app-container">
	  <AppTitle />
	  <VocabList vocabList={vocabList}/>
	  <MicroblogForm />
      </div>
  )
}

export default App

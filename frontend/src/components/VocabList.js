import React from 'react'

function VocabList(props){
  const vocabItems = props.vocabList.map(item => {
    return(
      <button key={item.id}className="vocab-button">{item.text}</button>
    )
  })
  return <div className="vocab-container">{vocabItems}</div>
}

export default VocabList

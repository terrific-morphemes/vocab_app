import React from 'react'

function VocabList(props){
  const vocabItems = props.vocabList.map(item => {
    return(
      <button key={item.id}className="vocab-button">{item.text}</button>
    )
  })
  return(
	  <div className="vocab-container">
	    <div className="vocab-callout">My vocab</div>
	    <div className="vocab-buttons">
		{vocabItems}
	    </div>
	  </div>
  )
}

export default VocabList

document.querySelector('#add_item').addEventListener('click', function() {
    // Create a new list item
    const newItem = document.createElement('li');
  
    // Set its text content to "Item"
    newItem.textContent = 'Item';
  
    // Find the unordered list with class "my_list"
    const list = document.querySelector('.my_list');
  
    // Append the new list item to the list
    list.appendChild(newItem);
  });
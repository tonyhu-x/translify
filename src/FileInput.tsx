export default function FileInput() {

  const readFile = (e) => {
    const curFiles = e.target.files;
    if (curFiles.length >= 0) {
      const reader = new FileReader();
      reader.onload = (ev) => {
        console.log(ev.target.result);
      };
      reader.readAsText(curFiles[0]);
    }
  };
  
  return (
    <input type="file" accept=".txt" onChange={readFile}/>
  );
}
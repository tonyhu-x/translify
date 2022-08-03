export default function FileInput() {

  const readFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    // curFiles cannot be null because this function is only called
    // as callback from user interacting with the input
    const curFiles = e.target.files!;
    if (curFiles.length >= 0) {
      const reader = new FileReader();
      reader.onload = (ev: ProgressEvent<FileReader>) => {
        console.log(ev.target!.result);
      };
      reader.readAsText(curFiles[0]);
    }
  };
  
  return (
    <input type="file" accept=".txt" onChange={readFile}/>
  );
}
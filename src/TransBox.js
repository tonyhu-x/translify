export default function TransBox({ out, onChange }) {

  const onTextChange = (e) => {
    onChange(e.target.value);
  };
  
  return (
    <textarea className="font-sans shadow" disabled={out} onChange={onTextChange}></textarea>
  );
};
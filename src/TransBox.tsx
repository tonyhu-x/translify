type TransBoxProps = {
  text: string;
  out?: boolean;
  onChange: (arg: string) => void;
};

export default function TransBox(props: TransBoxProps) {
  const text = props.text;
  const out = props.out;
  const onChange = props.onChange;

  const onTextChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    onChange(e.target.value);
  };
  
  return (
    <textarea className="font-sans shadow" disabled={out} onChange={onTextChange} value={text}></textarea>
  );
};
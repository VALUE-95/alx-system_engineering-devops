```markdown
# 0x06. Regular Expression (Regex) DevOps

## Table of Contents

- [Description](#description)
- [Concepts](#concepts)
- [Background Context](#background-context)
- [Resources](#resources)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Description

Ongoing second chance project - started Jan 30, 2024, 6:00 AM, must end by Feb 3, 2024, 6:00 AM. An auto review will be launched at the deadline.

## Concepts

For this project, the focus is on the following concept:

- Regular Expression

## Background Context

For this project, you are required to build your regular expression using Oniguruma, a regular expression library used by Ruby by default. The Ruby code snippet below demonstrates how to use regular expressions:

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
```

Replace the `regexp` part within the `//` with your regular expression. Example usage:

```bash
$ ./example.rb 127.0.0.2
127.0.0.2
$ ./example.rb 127.0.0.1
127.0.0.1
$ ./example.rb 127.0.0.a
```

### Resources

Read or watch:

- [Regular expressions - basics](link-to-basics)
- [Regular expressions - advanced](link-to-advanced)
- [Rubular is your best friend](link-to-rubular)
- [Use a regular expression against a problem: now you have 2 problems](link-to-problems)
- [Learn Regular Expressions with simple, interactive exercises](link-to-exercises)

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
- All your regex must be built for the Oniguruma library

## Usage

Provide instructions on how to use the regular expression in your project.

## Contributing

Explain how others can contribute to your project. Include guidelines for submitting issues or pull requests.

## License

Specify the license under which your project is distributed.

## Acknowledgments

Give credit to any resources, libraries, or individuals that inspired or contributed to your project.
```

Make sure to replace the placeholder links (`link-to-basics`, etc.) with the actual URLs of the resources you want to refer to in the "Resources" section.

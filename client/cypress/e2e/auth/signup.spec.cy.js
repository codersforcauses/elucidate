describe('Signup', () => {
  beforeEach(() => {
    cy.visit('signup');
  });
  it('can signup', () => {
    cy.get('input[name="First Name"').type('John');
    cy.get('input[name="Last Name"').type('Doe');
    cy.get('input[name="Email"').type('john.doe@example.com');
    cy.get('input[name="Password"').type('password');
    cy.get('input[name="Confirm Password"').type('password');
    cy.get('select').select('Grade 12');
    cy.get('button').should('not.have.attr', 'disabled');
    cy.get('button').click();
  });
});
